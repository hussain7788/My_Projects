import React from "react";

interface TableProps {
    columns : any[];
    data : any[];
}
const TableComponent = ({columns, data}: TableProps) => {

    return (
        <div className="table-container">
        <table className="table">
          <thead>
            <tr>
              <th>No</th>
              {columns.map((column, index) => (
                <th key={index}>{column}</th>
              ))}
            </tr>
          </thead>
        <tbody>
            {data.map((tag, ind) => (
                <tr key={ind}>
                  <td>{ind + 1}</td> 
                <td>{tag.hashtag}</td>
                <td>{tag.clicks}</td>
                </tr>
            ))}
          </tbody>
    </table>
    </div>
    )
}

export default TableComponent;