import './App.css';
import React from "react";
import axios, {AxiosResponse} from 'axios';
import {get, post, del, getCancelToken} from './backendinterface.ts';

interface ITodoItems {
  id:number,
  t_name:string,
  t_cr_date:string,
  t_due_date:string,
  t_completed:boolean
}

interface ITodoItemsFetch extends AxiosResponse{
  data: ITodoItems[]
}

interface ITodoItemsCreate extends AxiosResponse{
  data: ITodoItems
}

const ENDPOINT = "http://127.0.0.1:8000/todo/"

function App() {

  const [todoListData, setTodoListData] = React.useState<ITodoItems[]>([]);
  const [taskName , setTaskName] = React.useState("");
  const [filterValue , setFilterValue] = React.useState("")
  const cancelTokenSource = React.useRef(getCancelToken());

  React.useEffect(() => {
    let queryParams = {};
    const requestResponse = get(ENDPOINT, cancelTokenSource.current.token) as Promise<ITodoItemsFetch>;
    requestResponse.then((response) => {
        console.log("request data::", response.data);
        setTodoListData(response.data);
    })
}, [])

  

  function todoListItemsDisplay() {
    return (
      <ul>
        {todoListData.map((item) => {
          return(
            <li key={item.id}>
            <ul>
            <li>Task Name : {item.t_name}</li>
            <li>Task Date : {item.t_cr_date}</li>
            <li>Task Due Date : {item.t_due_date}</li>

            {(() => {
              if (item.t_completed){
                return <li style={{color:'blue'}}>Task is Completed</li>
              } else{
                return (
                  <li>
                    <p style={{color:'red'}}>Not Completed</p>
                    <input type='checkbox' onClick={(e) => todoItemMarkComplete(item.id)} />;
                  </li>
                ) 
              }
            })()}
            <button onClick={(e) => todoItemsDelete(item.id)} style={{color:'green'}}>Delete</button>

            </ul>
            </li>
          )
        })}
      </ul>
    )

  }
  function todoListAddSubmit(){
    let query_params = {
      section : 'create'
    }
    let formData = new FormData();
    formData.append("task_name", taskName);
    console.log("task name::", taskName)
    const requestResponse = post(ENDPOINT, formData, cancelTokenSource.current.token, query_params) as Promise<ITodoItemsCreate>;
    requestResponse.then((response) => {
        console.log("response data::", response.data);
        setTodoListData((prevTodoListItems) => {
          let newTodoListItems = [...prevTodoListItems, response.data];
          return newTodoListItems;
        });
    });
    setTaskName('') 
  }

  function todoItemMarkComplete(todoItemId: number){
    console.log("todoItemd::", todoItemId)
    let query_params = {
      section : 'mark_completed'
    }
    let formData = new FormData();
    formData.append("todo_item_id", todoItemId.toString());
    const requestResponse = post(ENDPOINT, formData, cancelTokenSource.current.token, query_params) as Promise<ITodoItemsCreate>;
    requestResponse.then((response) => {
        console.log("request data::", response.data);
        console.log("todoListData", todoListData)
        setTodoListData((prevTodoListItems) => {
          let newTodoListItems = [...prevTodoListItems];
          let replaceIndex = newTodoListItems.findIndex(item => item.id == todoItemId);
          newTodoListItems[replaceIndex] = response.data;
          return newTodoListItems;
        });
    }) 

  }

  function todoItemsDelete(todoItemId: number){
    let D_ENDPOINT = "http://127.0.0.1:8000/todo/" + todoItemId
    let query_params = {
    }

    const requestResponse = del(D_ENDPOINT, query_params);
    requestResponse.then((response) => {
        console.log("request data::", response.data);
        setTodoListData(response.data)
    }) 


  }

  function todoItemsFilter(){
    let query_params = {
      section : "filter"
    }
    let formData = new FormData();
    formData.append("filter_value", filterValue);

    const requestResponse = post(ENDPOINT, formData, cancelTokenSource.current.token, query_params) as Promise<ITodoItemsFetch>;
    requestResponse.then((response) => {
        console.log("request data::", response.data);
        setTodoListData(response.data)
    }) 

  }

  function todoListItemsAdd() {
    return(
      <React.Fragment>
      <input type="text" value={taskName} onChange={(e) => setTaskName(e.target.value)} />
      <button onClick={todoListAddSubmit}>Add Task</button>
      <div>
        <select value={filterValue} onChange={(e) => setFilterValue(e.target.value)}>
          <option value="all_tasks">All Tasks</option>
          <option value="completed">Completed Tasks</option>
          <option value="pending">Pending Tasks</option>
        </select>
        <button onClick={todoItemsFilter}>Search</button>
        <br></br>
      </div>
      </React.Fragment>
    )
  }

  
  return (
    <div className="App">
      <p>Todo List Items</p>
      {todoListItemsAdd()}
      {todoListItemsDisplay()}
      
    </div>
  );
}

export default App;
