import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

//Components
import { LoginComponent } from "./components/login/login.component";
import { RegistrarFuncionarioComponent } from "./components/registrar-funcionario/registrar-funcionario.component";
import { VisualizarFuncionariosComponent } from './components/visualizar-funcionarios/visualizar-funcionarios.component';
import { PerfilFuncionarioComponent } from './components/perfil-funcionario/perfil-funcionario.component';
import { VisualizarParqueosComponent } from './components/visualizar-parqueos/visualizar-parqueos.component';
import { RegistrarParqueoComponent } from './components/registrar-parqueo/registrar-parqueo.component';
import { FuncionarioComponent } from './components/funcionario/funcionario.component';
import { RegistrarPlacaComponent } from './components/registrar-placa/registrar-placa.component';
//Guards
import { AuthGuard } from "./auth.guard";
import { AuthFuncionarioGuard } from './auth-funcionario.guard';
import { RegistrarHorarioComponent } from './components/registrar-horario/registrar-horario.component';
import { RealizarReservacionComponent } from './components/realizar-reservacion/realizar-reservacion.component';
import { ConsultarDatosFuncionarioComponent } from './components/consultar-datos-funcionario/consultar-datos-funcionario.component';
import { InformeFuncionariosComponent } from './components/informe-funcionarios/informe-funcionarios.component';
import { InformeEstacionamientoComponent } from './components/informe-estacionamiento/informe-estacionamiento.component';
import { EstadisticasHorariosComponent } from './components/estadisticas-horarios/estadisticas-horarios.component';
import { VisualizarPlacasComponent } from './components/visualizar-placas/visualizar-placas.component';
import { EditarHorarioComponent } from './components/editar-horario/editar-horario.component';
import { ReservacionesComponent } from './components/reservaciones/reservaciones.component';
import { VisualizarReservacionesComponent } from './components/visualizar-reservaciones/visualizar-reservaciones.component';
import { SimuladorComponent } from './components/simulador/simulador.component';
import { HistorialReservasComponent } from './components/historial-reservas/historial-reservas.component';

const routes: Routes = [
  { 
    path: '', 
    redirectTo: '/login',
    pathMatch: 'full',
  },
  { 
    path: 'login',
    component: LoginComponent },
  {
    path: 'visualizarFuncionarios',
    component: VisualizarFuncionariosComponent,
    canActivate: [AuthGuard]
  },    
  {
    path: 'perfilFuncionario/:id',
    component: PerfilFuncionarioComponent,
    canActivate: [AuthGuard]
  }, 
  {
    path: 'registrarFuncionario',
    component: RegistrarFuncionarioComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'editarFuncionario/:id',
    component: RegistrarFuncionarioComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'editarFuncionario',
    component: RegistrarFuncionarioComponent,
    canActivate: [AuthGuard]

  },
  {
    path: 'parqueos',
    component: VisualizarParqueosComponent,
    canActivate: [AuthGuard]

  },
  {
    path: 'visualizarReservas',
    component: VisualizarReservacionesComponent,
    canActivate: [AuthGuard]
  },   
  {
    path: 'registrarParqueo',
    component: RegistrarParqueoComponent,
    canActivate: [AuthGuard]

  },
  {
    path: 'editarParqueo/:id',
    component: RegistrarParqueoComponent,
    canActivate: [AuthGuard]
  },

  {
    path: 'consultarDatosFuncionario',
    component: ConsultarDatosFuncionarioComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'informeFuncionarios',
    component: InformeFuncionariosComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'informeEstacionamientos',
    component: InformeEstacionamientoComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'estadisticasHorarios',
    component: EstadisticasHorariosComponent,
    canActivate: [AuthGuard]
  },     
  {
    path: 'inicio',
    component: FuncionarioComponent,
    canActivate: [AuthFuncionarioGuard]
  },
  {
    path: 'horario',
    component: RegistrarHorarioComponent,
    canActivate: [AuthFuncionarioGuard]
  },
  {
    path: 'realizarReservacion',
    component: RealizarReservacionComponent,
    canActivate: [AuthFuncionarioGuard]
  },
  {
    path: 'placas/:id',
    component: VisualizarPlacasComponent,
    canActivate: [AuthFuncionarioGuard]
  },
  {
    path: 'editarPlaca/:id/:codigoPlaca',
    component: RegistrarPlacaComponent,
    canActivate: [AuthFuncionarioGuard]
  },  
  {
    path: 'registrarplacas/:id',
    component: RegistrarPlacaComponent,
    canActivate: [AuthFuncionarioGuard]
  },
  {
    path: 'editarHorario/:id',
    component: EditarHorarioComponent,
    canActivate: [AuthFuncionarioGuard]
  },
  {
    path: 'reservar/:idFuncionario/:idParqueo',
    component: ReservacionesComponent,
    canActivate: [AuthFuncionarioGuard]
  },
  {
    path: 'reserva',
    component: ReservacionesComponent,
    canActivate: [AuthFuncionarioGuard]
  },
  {
    path: 'reserva/id',
    component: ReservacionesComponent,
  },
  {
    path: 'simular',
    component: SimuladorComponent,
    canActivate: [AuthFuncionarioGuard]
  },
  {
    path: 'historialReservas',
    component: HistorialReservasComponent,
    canActivate: [AuthFuncionarioGuard]
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
