import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { BusComponent } from './travel/bus/bus.component';
import { AboutusComponent } from './aboutus/aboutus.component';
import { ContactComponent } from './contact/contact.component';
import { LoginComponent } from './login/login.component';
import { BannerComponent } from './banner/banner.component';
import { FooterComponent } from './footer/footer.component';
import { RegisterComponent } from './register/register.component';
import { AuthGuard } from './auth.guard';



const routes: Routes = [
  {path:'',redirectTo:'',pathMatch:'full'},
  {path:'aboutus',component:AboutusComponent},
  {path:'contact',component:ContactComponent},
  {path:'banner',component:BannerComponent},
  {path:'footer',component:FooterComponent},
  {path:'register',component:RegisterComponent,canActivate:[AuthGuard]},
  {path:'login',component:LoginComponent},
  {path:'home',component:HomeComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

