import { Component, OnInit, ElementRef } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { FacadeService } from 'src/app/services/facade.service';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent   implements OnInit {
  showAlert = false;
  showPassword = false;
  succesLogin = true;
  loginForm =  this.formBuilder.group({
    correo: ['', [Validators.required, Validators.email]],
    contraseña: ['', [Validators.required]]
  });

  constructor( 
    private formBuilder: FormBuilder,
    public facadeService: FacadeService,
  ) { }

  ngOnInit(): void {

  }

  // Muestra la alerta de error o la esconde
  toggleAlert(value:boolean): void {
      this.showAlert = value;
  }

  togglePassword(): void {
    this.showPassword = !this.showPassword;
  }

  login(): void {
    this.facadeService.login(this.loginForm.value)
    if (this.loginForm.invalid) {
      this.toggleAlert(true);
    }else if(!this.succesLogin) {
      this.toggleAlert(true);
    }
  }
}

