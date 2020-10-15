import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { IniciarComponent } from './components/iniciar/iniciar.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { RegistroComponent } from './components/registro/registro.component';
import { RegistroMedicoComponent } from './components/registro-medico/registro-medico.component';

@NgModule({
  declarations: [
    AppComponent,
    IniciarComponent,
    NavbarComponent,
    RegistroComponent,
    RegistroMedicoComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
