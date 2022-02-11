import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AddbusComponent } from './addbus/addbus.component';
import { StateComponent } from './state/state.component';
import { CityComponent } from './city/city.component';
import { BusComponent } from './bus/bus.component';
import { HeadComponent } from './head/head.component';
import { FootComponent } from './foot/foot.component';


const routes: Routes = [
  {path:'buslist',component:BusComponent},
  {path:'addbus',component:AddbusComponent},
  {path:'state',component:StateComponent},
  {path:'city',component:CityComponent},
  {path:'head',component:HeadComponent},
  {path:'foot',component:FootComponent},
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TravelRoutingModule { }
