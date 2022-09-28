import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LoginComponent } from './components/login/login.component';
import { RegistrarFuncionarioComponent } from './components/registrar-funcionario/registrar-funcionario.component';
import { SolicitarNotificacionesComponent } from './components/solicitar-notificaciones/solicitar-notificaciones.component';
import { ToolbarComponent } from './components/toolbar/toolbar.component';
import {VerInformeHorariosComponent} from "./components/ver-informe-horarios/ver-informe-horarios.component";
// Forms
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { RegistrarParqueoComponent } from './components/registrar-parqueo/registrar-parqueo.component';
import { RegistrarPlacaComponent } from './components/registrar-placa/registrar-placa.component';
import { RegistrarHorarioComponent } from './components/registrar-horario/registrar-horario.component';
import { HttpClientModule } from '@angular/common/http';

// Protege el acceso a la página
import { AuthGuard } from './auth.guard';
import { VisualizarFuncionariosComponent } from './components/visualizar-funcionarios/visualizar-funcionarios.component';
import { PerfilFuncionarioComponent } from './components/perfil-funcionario/perfil-funcionario.component';
import { VisualizarPlacasComponent } from './components/visualizar-placas/visualizar-placas.component';
import { VisualizarParqueosComponent } from './components/visualizar-parqueos/visualizar-parqueos.component';
import { FuncionarioComponent } from './components/funcionario/funcionario.component';
import { RealizarReservacionComponent } from './components/realizar-reservacion/realizar-reservacion.component';
import { ConsultarDatosFuncionarioComponent } from './components/consultar-datos-funcionario/consultar-datos-funcionario.component';
import { FuncionarioFilterPipe } from './pipes/funcionario-filter.pipe';
import { InformeFuncionariosComponent } from './components/informe-funcionarios/informe-funcionarios.component';
import { InformeFuncionariosPipe } from './pipes/informe-funcionarios.pipe';
import { EstadisticasHorariosComponent } from './components/estadisticas-horarios/estadisticas-horarios.component';
import { InformeEstacionamientoComponent } from './components/informe-estacionamiento/informe-estacionamiento.component';
import { EditarHorarioComponent } from './components/editar-horario/editar-horario.component';
import { AuthService } from './services/auth.service';
import { FuncionariosService } from './services/funcionarios.service';
import { EscuelasService } from './services/escuelas.service';
import { HorarioService } from './services/horario.service';
import { ParqueoService } from './services/parqueo.service';
import { PlacasService } from './services/placas.service';
import { TPService } from './services/tipo-parqueo.service';
import { FacadeService } from './services/facade.service';
import { ReservacionesComponent } from './components/reservaciones/reservaciones.component';
import { VisualizarReservacionesComponent } from './components/visualizar-reservaciones/visualizar-reservaciones.component';
import { ParqueoFilterPipe } from './pipes/parqueo-filter.pipe';
import { SimuladorComponent } from './components/simulador/simulador.component';
import { HistorialReservasComponent } from './components/historial-reservas/historial-reservas.component';
import { HistorialReservasFilterPipe } from './pipes/historial-reservas-filter.pipe';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegistrarFuncionarioComponent,
    SolicitarNotificacionesComponent,
    ToolbarComponent,
    SidebarComponent,
    VisualizarFuncionariosComponent,
    VerInformeHorariosComponent,
    RegistrarParqueoComponent,
    RegistrarPlacaComponent,
    RegistrarHorarioComponent,
    PerfilFuncionarioComponent,
    VisualizarPlacasComponent,
    VisualizarParqueosComponent,
    FuncionarioComponent,
    RealizarReservacionComponent,
    ConsultarDatosFuncionarioComponent,
    FuncionarioFilterPipe,
    InformeFuncionariosComponent,
    InformeFuncionariosPipe,
    EstadisticasHorariosComponent,
    InformeEstacionamientoComponent,
    EditarHorarioComponent,
    ReservacionesComponent,
    VisualizarReservacionesComponent,
    ParqueoFilterPipe,
    SimuladorComponent,
    HistorialReservasComponent,
    HistorialReservasFilterPipe,
    

  ],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule
  ],
  providers: [
    AuthGuard,
    AuthService,
    FuncionariosService,
    EscuelasService,
    HorarioService,
    ParqueoService,
    PlacasService,
    TPService,
    FacadeService,
    LoginComponent
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
