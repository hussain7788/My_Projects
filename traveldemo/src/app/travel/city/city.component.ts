import { Component, OnInit } from '@angular/core';
import { StateserviceService } from 'src/app/stateservice.service';

@Component({
  selector: 'app-city',
  templateUrl: './city.component.html',
  styleUrls: ['./city.component.css']
})
export class CityComponent implements OnInit {
    cityid:any;
    cityname:any;
    select:any;
    citylist:any;
    city:any;
    citydata:any;
  constructor(private reg:StateserviceService) { }

  ngOnInit(): void {
    this.reg.getcity().subscribe(res=>
      {
        this.citylist=res
      })
      this.reg.getuser().subscribe(res=>
        {
          this.city=res
        })
  }
  
  onSubmit()
  {
    this.citydata={id:this.cityid,cityname:this.cityname,state:this.select};
    this.reg.savecity(this.citydata).subscribe(res=>
      {
        this.reg.getcity().subscribe(res=>
          {
            this.citylist=res
          })
      })
  }
  deletecity(id:number)
  {
    this.reg.delcity(id).subscribe(res=>
      {
        this.ngOnInit();
      })
  }
  


}
