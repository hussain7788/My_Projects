import { Component, OnInit } from '@angular/core';
import { Bus } from 'src/app/model/busdetails.model';

@Component({
  selector: 'app-bus',
  templateUrl: './bus.component.html',
  styleUrls: ['./bus.component.css']
})
export class BusComponent implements OnInit {
    busdetails:Bus[]=[
      {
        sno:101,
        from_to:'hyd to kadapa',
        timings:'8pm_6am',
        capacity:40,
        fare:500,
        photopath:'assets/bg3.png'
      },
      {
        sno:2001,
        from_to:'vizag_hyderabad',
        timings:'5pm_3am',
        capacity:40,
        fare:600,
        photopath:'assets/bg2.png'
      },
      {
        sno:3002,
        from_to:'chennai_vizag',
        timings:'9pm_5am',
        capacity:40,
        fare:400,
        photopath:'assets/bg1.png'
      },
      {
        sno:4002,
        from_to:'kurnool_kadapa',
        timings:'10pm_5am',
        capacity:40,
        fare:600,
        photopath:'assets/bg4.png'
      }
    ]
  constructor() { }

  ngOnInit(): void {
  }

}
