
import { Injectable } from '@angular/core';
import { HttpClientModule,HttpClient, HttpHeaders } from '@angular/common/http';
import {observable, Observable} from 'rxjs'
import { State } from '../../../traveldemo/src/app/model/state.model';
const headerOption={
  headers:new HttpHeaders({'content-Type':'application/json'})
}
@Injectable({
  providedIn: 'root'
})
export class StateserviceService {

  constructor(private http:HttpClient) { }
  saveuser(empform:any)
  {
    return this.http.post("http://localhost:3000/state",empform);
  }
  
  getuser()
  {
    return this.http.get("http://localhost:3000/state");
  }
  getcity()
  {
    return this.http.get("http://localhost:3000/city");
  }
  savecity(cityform:any)
  {
    return this.http.post("http://localhost:3000/city",cityform);
  }
  
  getbus()
  {
    return this.http.get("http://localhost:3000/travel")
  }
  savebus(busform:any)
  {
    return this.http.post("http://localhost:3000/travel",busform); 
  }
//   SearchEmpById(id:number)
//   {
//       return this.http.get("http://localhost:3000/state"+id);
//   }
//   DeleteEmp(id:number)
//   {
//     return this.http.delete("http://localhost:3000/state"+id);
//   }
//   updateuser(formdata:any)
//   {
//     debugger
//     return this.http.put("http://localhost:3000/state"+formdata.id,formdata);
//   }

  mockurl="http://localhost:3000/state"
  deletestate(id:number):Observable<State[]>
  {
        return this.http.delete<State[]>(this.mockurl+'/'+id,headerOption);
  }
  travelurl="http://localhost:3000/travel"
  delbus(id:number)
  {
    return this.http.delete(this.travelurl+'/'+id);
  }
  cityurl="http://localhost:3000/city"
  delcity(id:number)
  {
    return this.http.delete(this.cityurl+'/'+id);
  }
  isuserlog()
  {
    alert("not authentiated user");
    return true;
  }

}

