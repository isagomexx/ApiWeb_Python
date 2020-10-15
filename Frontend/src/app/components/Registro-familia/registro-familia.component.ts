import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-registro-familia',
  templateUrl: './registro-familia.component.html',
  styleUrls: ['./registro-familia.component.css']
})
export class RegistroFamiliaComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit(): void {
  }
  
  inicio(){
    this.router.navigate(['/Iniciar'])
    }
}
