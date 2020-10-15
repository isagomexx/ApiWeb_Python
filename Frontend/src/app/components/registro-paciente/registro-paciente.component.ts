import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-registro-paciente',
  templateUrl: './registro-paciente.component.html',
  styleUrls: ['./registro-paciente.component.css']
})
export class RegistroPacienteComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit(): void {
  }
  inicio(){
    this.router.navigate(['/Inicio'])
    }
}
