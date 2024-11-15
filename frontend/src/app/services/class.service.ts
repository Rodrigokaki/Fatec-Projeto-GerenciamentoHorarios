import { Injectable } from '@angular/core';
import { IClass } from '../models/IClass';
import { HttpClient } from '@angular/common/http';
import { forkJoin, map, Observable, switchMap } from 'rxjs';
import { IClassName } from '../models/IClassName';
import { CourseService } from './course.service';

@Injectable({
  providedIn: 'root'
})
export class ClassService {

  url = "http://127.0.0.1:5000/classes";

  private sharedClass: IClass = {} as IClass;

  constructor(private http: HttpClient, private courseService: CourseService) { }

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

  getClassesWithName(): Observable<IClassName[]> {
    return this.getClasses().pipe(
      map(turmas =>
        turmas.map(turma => {
          return this.courseService.getCourseId(turma.cod_curso).pipe(
            map(curso => ({
              ...turma,
              nome_curso: curso.nome,
            }))
          );
        })
      ),
      switchMap(observables => forkJoin(observables))
    );
  }  
}
