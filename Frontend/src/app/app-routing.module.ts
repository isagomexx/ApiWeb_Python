import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { IniciarComponent } from './components/iniciar/iniciar.component';
import { RegistroComponent } from './components/registro/registro.component';
import { RegistroMedicoComponent } from './components/registro-medico/registro-medico.component';
import { RegistroPacienteComponent } from './components/registro-paciente/registro-paciente.component';
import { RegistroFamiliaComponent } from './components/Registro-familia/registro-familia.component';


const routes: Routes = [
  { path: 'Iniciar', component: IniciarComponent },
  { path: 'Registro', component: RegistroComponent },
  { path: 'Registro-medico', component: RegistroMedicoComponent },
  { path: 'Registro-paciente', component: RegistroPacienteComponent},
  { path: 'Registro-familia', component: RegistroFamiliaComponent},
  { path: '**', pathMatch: 'full', redirectTo: 'Iniciar'},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
