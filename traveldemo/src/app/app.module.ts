
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from '../../../traveldemo/src/app/header/header.component';
import { BannerComponent } from '../../../traveldemo/src/app/banner/banner.component';
import { FooterComponent } from '../../../traveldemo/src/app/footer/footer.component';
import { LoginComponent } from '../../../traveldemo/src/app/login/login.component';
import { HomeComponent } from '../../../traveldemo/src/app/home/home.component';
import { AboutusComponent } from '../../../traveldemo/src/app/aboutus/aboutus.component';
import { ContactComponent } from '../../../traveldemo/src/app/contact/contact.component';
import { TravelModule } from '../../../traveldemo/src/app/travel/travel.module';
import {FormsModule} from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { StateserviceService } from './stateservice.service';
import { RegisterComponent } from '../../../traveldemo/src/app/register/register.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    BannerComponent,
    FooterComponent,
    LoginComponent,
    HomeComponent,
    AboutusComponent,
    ContactComponent,
    RegisterComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    TravelModule,
    FormsModule,
    HttpClientModule,
  
  ],
  
  providers: [StateserviceService],
  bootstrap: [AppComponent]
})
export class AppModule { }

