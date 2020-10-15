import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent implements OnInit {

  constructor(private router: Router) { 

  }

  ngOnInit(): void {
  }
medico(){
this.router.navigate(['/Registro-medico'])
}

paciente(): void {
  this.router.navigate(['/Registro-paciente'])
}
}
