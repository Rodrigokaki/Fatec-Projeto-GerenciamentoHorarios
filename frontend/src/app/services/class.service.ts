import { Injectable } from '@angular/core';
import { IClass } from '../models/IClass';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ClassService {

  url = "http://127.0.0.1:5000/classes";

  private sharedClass: IClass = {} as IClass;

  constructor(private http: HttpClient) { }

  getSharedClass(): IClass {
    return this.sharedClass;
  }

  setSharedClass(classObj: IClass): void {
    this.sharedClass = classObj;
  }

  getClasses(): Observable<IClass[]> {
    return this.http.get<IClass[]>(this.url);
  }

  getClassId(classObjId: number): Observable<IClass> {
    return this.http.get<IClass>(`${this.url}/${classObjId}`);
  }

  saveClass(classObj: IClass): Observable<IClass> {
    return this.http.post<IClass>(this.url, classObj);
  }

  deleteClass(classObj: IClass): Observable<void> {
    return this.http.delete<void>(`${this.url}/${classObj.cod_turma}`);
  }

  updateClass(classObj: IClass): Observable<IClass> {
    return this.http.put<IClass>(`${this.url}/${classObj.cod_turma}`, classObj);
  }
}
