import { Component, OnInit } from '@angular/core';
import { StateserviceService } from '../stateservice.service';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
    id:any;
    name:any;
    address:any;
    gender:any;
    username:any;
    password:any;
    regdata:any;
    reglist:any;
  constructor(private reg:StateserviceService) { }

  
  ngOnInit(): void {
  }
  save(register:NgForm)
  {
    console.log(register)
  }

}
