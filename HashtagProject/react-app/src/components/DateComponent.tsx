
import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import {get} from '../backendinterface.ts';
import { AxiosResponse } from 'axios';
import TableComponent from './TableComponent.tsx';


interface TableData extends AxiosResponse{
  data : {
    columns : any[];
    data : any[];

  }
}

const ENDPOINT = "http://127.0.0.1:8000/hashtags/"

const DateComponent = () => {
  const [startDate, setStartDate] = React.useState('');
  const [endDate, setEndDate] = React.useState('');
  const [tableData, setTableData] = React.useState<TableData>();
  const [columns, setColumns] = React.useState([]);
  const [data, setData] = React.useState([]);
  const [error, setError] = React.useState<string | null>(null);


  const handleSubmit = async () => {
  
    let query_params = {
      section: 'get_hashtags',
      start_date: startDate,
      end_date: endDate
    }
    try{
    const resp = await get(ENDPOINT, query_params) as Promise<TableData>
    setColumns(resp.data.columns);
    setData(resp.data.data);
    setTableData(resp.data);
    setError(null);
  } catch(error){
    setError(`${error.response.data.message}`);
    setTableData(undefined);
  }
}

  const showButton = () => {
    return (
      startDate && endDate ? <button onClick={handleSubmit}>Search</button> : 
                             <button>Search</button>
    )
  }

    return (
    <div>
      <h3>Find Top Hashtags</h3>
        <DatePicker
            selected={startDate}
            onChange={(date) => setStartDate(date)}
            placeholderText={startDate ? undefined : 'Select a start date'}
            dateFormat="dd/MM/yyyy"
      />
      <DatePicker
            selected={endDate}
            onChange={(date) => setEndDate(date)}
            placeholderText={endDate ? undefined : 'Select a end date'}
            dateFormat="dd/MM/yyyy"
      />
      {showButton()}
      {tableData && <TableComponent columns={columns} data={data} />}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
    )
};


export default DateComponent;