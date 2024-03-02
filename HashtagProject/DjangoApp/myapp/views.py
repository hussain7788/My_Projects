from django.shortcuts import render
from rest_framework.decorators import api_view
import pandas as pd
import os
from rest_framework.response import Response
from dateutil import parser


def read_csv_file():
    """
        Reading CSV file and 
        converting into dataframe
    """
    main_dir = os.path.dirname(__file__)
    file_path = os.path.join(main_dir, 'files', 'top_hashtags_data.csv')
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return df

def parse_dates(start_date, end_date):
    """
        Parse dates and convert to local time
    """
    start_date = pd.to_datetime(parser.parse(start_date)). \
                                tz_convert('Asia/Kolkata')
    end_date = pd.to_datetime(parser.parse(end_date)).\
                                tz_convert('Asia/Kolkata')
    return start_date, end_date

@api_view(['GET'])
def get_top_hashtags(request):
    if request.query_params.get('section', None) == 'get_hashtags':
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)
        if start_date and end_date:
            try:
                data_frame = read_csv_file()
                if not data_frame.empty:
                    data_frame['DateTime'] = pd.to_datetime(data_frame['DateTime'], 
                                                            errors='coerce', 
                                                            format='%Y-%m-%d %H:%M:%S', 
                                                            infer_datetime_format=True)
                    start_date, end_date = parse_dates(start_date, end_date)
                    data_frame['DateTime'] = data_frame['DateTime'].dt.tz_localize('Asia/Kolkata')
                    data_frame.dropna(inplace=True)
                    data_frame['DateTime'] = data_frame['DateTime'].dt.floor('D')
                    df = data_frame[(data_frame['DateTime'] >= start_date) & 
                                    (data_frame['DateTime'] <= end_date)]
                    if not df.empty:
                        records = df.to_dict()
                        posts = [{
                                    'date_time': records['DateTime'][index],
                                    'post_content': records['PostContent'][index],
                                    'clicks': records['Clicks'][index]
                                    }
                                    for index, record in records['DateTime'].items()
                                ]
                        hashtags_count = {}
                        for post in posts:
                            hashtags = [word for word in post['post_content'].split() 
                                             if word.startswith('#')]
                            for hashtag in hashtags:
                                hashtags_count[hashtag] = hashtags_count.get(hashtag, 0) + post['clicks']
                        top_hashtags = sorted(hashtags_count.items(), 
                                              key=lambda x: x[1], 
                                              reverse=True)[:5]
                        data = [{'hashtag': hashtag, 'clicks': clicks}
                                    for hashtag, clicks in top_hashtags]
                        result = {"columns": ['Hashtags', 'Clicks'], 
                                    "data":data}
                        return Response(result, status=200)
                    else:
                        return Response({"message":"No data found for given duration"}, status=404)
                else:
                    return Response({"message":"Data not found"}, status=422)
            except Exception as err:
                return Response({"message": str(err)}, status=422)
        else:
            return Response({"message": "Please provide start and end dates"}, status=400)
    else:
        return Response({"message": "Please provide valide section"}, status=400)



