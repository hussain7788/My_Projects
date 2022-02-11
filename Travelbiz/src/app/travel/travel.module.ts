import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { TravelRoutingModule } from './travel-routing.module';
import { BusComponent } from './bus/bus.component';
import { AddbusComponent } from './addbus/addbus.component';
import { StateComponent } from './state/state.component';
import { CityComponent } from './city/city.component';
import { FormsModule } from '@angular/forms';
import { HeadComponent } from './head/head.component';
import { FootComponent } from './foot/foot.component';


@NgModule({
  declarations: [BusComponent, AddbusComponent, StateComponent, CityComponent, HeadComponent, FootComponent],
  imports: [
    CommonModule,
    TravelRoutingModule,
    FormsModule,
  ],
  exports:[BusComponent,AddbusComponent],
})
export class TravelModule { }
