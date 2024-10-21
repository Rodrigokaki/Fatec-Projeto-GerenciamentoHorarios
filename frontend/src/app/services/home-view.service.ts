import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { IHome } from '../models/IHome';

@Injectable({
  providedIn: 'root'
})
export class HomeViewService {

  url = "http://127.0.0.1:5000/home";

  constructor(private http: HttpClient) { }

  getView(): Observable<IHome[]> {
    return this.http.get<IHome[]>(this.url);
  }

  getViewByDay(day: number): Observable<IHome> {
    return this.http.get<IHome>(`${this.url}/${day}`);
  }
}
