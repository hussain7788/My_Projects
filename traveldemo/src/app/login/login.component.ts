import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  username:any;
  password:any;
  result:any;
  photopath:any;
  photopreview:any;
    constructor(private route:Router) { }
    

    
    
    ngOnInit(): void {
    }
    check()
    {
      if(this.username=="hussain" && this.password==12345)
      {
          // this.result="valid user"
          this.route.navigate(['/banner'])
      
      }
      else{
        this.result="invalid user"
      }
    }

}
