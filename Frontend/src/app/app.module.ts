import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { IniciarComponent } from './components/iniciar/iniciar.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { RegistroComponent } from './components/registro/registro.component';
import { RegistroMedicoComponent } from './components/registro-medico/registro-medico.component';
import { RegistroPacienteComponent } from './components/registro-paciente/registro-paciente.component';
import { RegistroFamiliaComponent } from './components/registro-familia/registro-familia.component';

@NgModule({
  declarations: [
    AppComponent,
    IniciarComponent,
    NavbarComponent,
    RegistroComponent,
    RegistroMedicoComponent,
    RegistroPacienteComponent,
    RegistroFamiliaComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
