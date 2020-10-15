import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpClientModule } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Paciente } from "src/app/entidades/paciente/paciente";
import { map } from "rxjs/operators";
@Injectable({
  providedIn: 'root'
})
export class PacienteService {
  private url="http://127.0.0.1:8000/";
  constructor(private httpClient:HttpClient) { }

  // registrarPaciente(paciente:Paciente):Observable<Paciente>{
  //   return this.http.post<Paciente>(this.url, paciente);
  // }

  public registrarPaciente(tipo_documento,numero_identificacion,nombres,apellido_paterno,apellido_materno,telefono,direccion,correo, estrato, fecha_nacimiento,id_grupo_familiar,id_doctor,usuario,contrasena) {
    return this.httpClient.post<any>(this.url + 'registropaciente', { tipo_documento,numero_identificacion,nombres,apellido_paterno,apellido_materno,telefono,direccion,correo, estrato, fecha_nacimiento,id_grupo_familiar,id_doctor,usuario,contrasena })
    .pipe(map(Users => {
    return Users;
    }));
    }

  }



