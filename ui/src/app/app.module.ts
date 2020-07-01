import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DockerImagesComponent } from './docker-images/docker-images.component';
import { DockerContainersComponent } from './docker-containers/docker-containers.component';

@NgModule({
  declarations: [
    AppComponent,
    DockerImagesComponent,
    DockerContainersComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
