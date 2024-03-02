import requests


class Test_hashtags():
    """
        Testing hashtag API from all scenarious
    """

    ENDPOINT = 'http://localhost:8000/hashtags/'
    query_params = {
            'section': 'get_hashtags',
            'start_date': '2024-01-23T18:30:00.000Z',
            'end_date': '2024-01-31T18:30:00.000Z'
        }

    def test_1_get_hashtags(self):
        """
            get top hashtags for the given date range
            asserting expecting status code with
            actual status code
        """
        resp = requests.get(self.ENDPOINT, 
                            params=self.query_params)
        assert(resp.status_code == 200)

    def test_2_invalid_date_range(self):
        """
            giving date range that not exist 
            asserting expecting error message with
            actual error message
        """
        query_params = self.query_params.copy()
        query_params['start_date'] = '2024-03-23T18:30:00.000Z'
        query_params['end_date'] = '2024-04-30T18:30:00.000Z'
        resp = requests.get(self.ENDPOINT,
                            query_params
                            )
        assert(resp.status_code == 404)
        assert(resp.json().get('message') == 'No data found for given duration')

    def test_3_validate_start_end_dates(self):
        """
            Testing without start and end dates in query params
            asserting expecting error message with
            actual error message
        """
        query_params = {
            'section': self.query_params['section']}
        resp = requests.get(self.ENDPOINT,
                            query_params
                            )
        assert(resp.status_code == 400)
        assert(resp.json().get('message') == 'Please provide start and end dates')
    
    def test_4_invalid_section(self):
        """
            Testing with invalid section in query params
            asserting expecting error message with
            actual error message
        """
        query_params = self.query_params.copy()
        query_params['section'] = 'invalid'
        resp = requests.get(self.ENDPOINT,
                            query_params
                            )
        assert(resp.status_code == 400)
        assert(resp.json().get('message') == 'Please provide valide section')


    

    