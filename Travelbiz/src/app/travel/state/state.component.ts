import { Component, OnInit } from '@angular/core';
import { StateserviceService } from 'src/app/stateservice.service';
import { State } from 'src/app/model/state.model';

@Component({
  selector: 'app-state',
  templateUrl: './state.component.html',
  styleUrls: ['./state.component.css']
})
export class StateComponent implements OnInit {
  stateid:any;
  statename:any;
  emplist:any;
  formdata:any;
  id:any;
  empdata:any;
  statelist:any;
  constructor(private reg:StateserviceService) { }

  ngOnInit(): void {
      this.getuser();
  }
  getuser()
  {
    this.reg.getuser().subscribe(res=>
      {
        this.statelist=res;
      })
  }
  
  onSubmit()
  {
    debugger
    this.formdata={id:this.id,stateid:this.stateid,statename:this.statename};
    this.reg.saveuser(this.formdata).subscribe(res=>
      {
        this.reg.getuser().subscribe(res=>
          {
            this.statelist=res
          })
      })
  };

  DeleteEmp(id:number)
  {
   this.reg.deletestate(id).subscribe(
    res=>
    {
      this.getuser();
    }
  )
    
  };


//   GetEmpById(id)
//   {
//   this.reg.SearchEmpById(id).subscribe(res=>
//     {
//       debugger
//       this.empdata=res;
//       this.id=this.empdata.id;
//       this.stateid=this.empdata.stateid;
//       this.statename=this.empdata.statename;
//     });
//   }

// getuser()
// {
//   this.reg.getuser().subscribe(res=>
//     {
//       this.statelist=res;
//     })
// }
// OnUpdate()
// {
//   debugger
//   this.formdata={id:this.id,stateid:this.stateid,statename:this.statename};
//   this.reg.updateuser(this.formdata).subscribe(res=>
//     {
//       this.getuser();
//     });

// }
}
