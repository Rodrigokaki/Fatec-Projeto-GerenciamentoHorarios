import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, NavigationEnd, Routes } from '@angular/router';
import { routes } from '../../app-routing.module';
import { Router } from '@angular/router';
import { Location } from '@angular/common';
import { filter } from 'rxjs';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent implements OnInit {
  constructor(private _router: Router) {}

  routes: Routes = routes;
  relativeRoutes: Map<string, string> = new Map<string, string>();

  ngOnInit(): void {
    this._router.events.subscribe((routerData) => {
      if(routerData instanceof NavigationEnd){

        const index = routerData.url.split("/")[1];

        for (let route of routes) {
          if (route.path?.split("/")[0] === index && route.path && route.data) {
            this.relativeRoutes.set(route.path, route.data['title']);
          }
        }
      }
    })

  }
}
