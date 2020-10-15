import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { IniciarComponent } from './components/iniciar/iniciar.component';
import { RegistroComponent } from './components/registro/registro.component';

const routes: Routes = [
  { path: 'Iniciar', component: IniciarComponent },
  { path: 'Registro', component: RegistroComponent },
  { path: '**', pathMatch: 'full', redirectTo: 'Iniciar'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
