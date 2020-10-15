import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-registro-medico',
  templateUrl: './registro-medico.component.html',
  styleUrls: ['./registro-medico.component.css']
})
export class RegistroMedicoComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit(): void {
  }
  inicio(){
    this.router.navigate(['/Inicio'])
    }
}
