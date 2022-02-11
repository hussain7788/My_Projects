import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { StateserviceService } from 'src/app/stateservice.service';

@Component({
  selector: 'app-addbus',
  templateUrl: './addbus.component.html',
  styleUrls: ['./addbus.component.css']
})
export class AddbusComponent implements OnInit {
buslist:any;
busdata:any;
    

    id:any;
    sno:any;
    from:any;
    to:any;
    deptime:any;
    arrtime:any;
    fare:any;
  constructor(private reg:StateserviceService) { }

  ngOnInit(): void
   {
      this.getbus();
  }
  getbus()
  {
    this.reg.getbus().subscribe(res=>
      {
        this.buslist=res
      }) 
  }
  onSubmit()
  {
    this.busdata={id:this.id,sno:this.sno,from:this.from,to:this.to,deptime:this.deptime,arrtime:this.arrtime,fare:this.fare};
    this.reg.savebus(this.busdata).subscribe(res=>
      {
        this.reg.getbus().subscribe(res=>
          {
            this.buslist=res;
          })
      })
  }

deletebus(id:number)
{
  console.log(id);
  this.reg.delbus(id).subscribe(res=>
    {
      this.getbus();
    })
}
}
