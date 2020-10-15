import { Component, OnInit } from '@angular/core';
import { Paciente } from 'src/app/entidades/paciente/paciente';
import { FormGroup, FormControl, FormBuilder, Validators, NgForm } from '@angular/forms';
import { PacienteService } from "src/app/servicios/paciente/paciente.service";
import { Router } from '@angular/router';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-registro-paciente',
  templateUrl: './registro-paciente.component.html',
  styleUrls: ['./registro-paciente.component.css']
})
export class RegistroPacienteComponent implements OnInit {
    angForm: FormGroup;
    paciente:Paciente= new Paciente();

    constructor(/*private fb: FormBuilder,private dataService: PacienteService,*/private router:Router){
    //   this.angForm = this.fb.group({
    //     tipo_documento : ['', [Validators.required,Validators.minLength(1)]],
    //     numero_identificacion: ['', Validators.required],
    //     nombres: ['', Validators.required],
    //     apellido_paterno: ['', Validators.required],
    //     apellido_materno: ['', Validators.required],
    //     telefono: ['', Validators.required],
    //     direccion: ['', Validators.required],
    //     correo: ['', Validators.required],
    //     estrato: ['', Validators.required],
    //     fecha_nacimiento: ['', Validators.required],
    //     id_grupo_familiar: ['', Validators.required],
    //     id_doctor: ['', Validators.required],
    //     usuario: ['', Validators.required],
    //     contrasena: ['', Validators.required],
    //   });
    }
    

  ngOnInit() {
    
  }

  // guardarPaciente(angForm1){
  //   this.dataService.registrarPaciente(angForm1.value.tipo_documento, angForm1.value.numero_identificacion, angForm1.value.nombres, angForm1.value.apellido_paterno, angForm1.value.apellido_materno,
  //                                     angForm1.value.telefono, angForm1.value.direccion, angForm1.value.correo, angForm1.value.estrato, angForm1.value.fecha_nacimiento, angForm1.value.id_grupo_familiar,
  //                                     angForm1.value.id_doctor,angForm1.value.usuario, angForm1.value.contrasena).pipe(first()).subscribe(data=>{this.router.navigate(['inicio']);},
  //                                     )
  // } 

   familia(){
     this.router.navigate(['/Registro-familia'])
     }

}

