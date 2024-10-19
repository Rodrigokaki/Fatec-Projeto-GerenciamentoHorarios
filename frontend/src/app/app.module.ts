import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SubjectComponent } from './pages/register/subject/subject.component';
import { TeacherComponent } from './pages/register/teacher/teacher.component';
import { LessonComponent } from './pages/register/lesson/lesson.component';
import { ClassComponent } from './pages/register/class/class.component';
import { StudentComponent } from './pages/register/student/student.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { NavbarComponent } from './navbar/navbar.component';
import { HomeComponent } from './pages/home/home.component';
import { CourseComponent } from './pages/register/course/course.component';

@NgModule({
  declarations: [
    AppComponent,
    SubjectComponent,
    TeacherComponent,
    LessonComponent,
    ClassComponent,
    StudentComponent,
    NavbarComponent,
    HomeComponent,
    CourseComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule
  ],
  providers: [
    provideClientHydration()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
