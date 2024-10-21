import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SubjectComponent } from './pages/subject/subject.component';
import { TeacherComponent } from './pages/teacher/teacher.component';
import { LessonComponent } from './pages/lesson/lesson.component';
import { ClassComponent } from './pages/class/class.component';
import { StudentComponent } from './pages/student/student.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { HomeComponent } from './pages/home/home.component';
import { CourseComponent } from './pages/course/course.component';
import { ClassRegisterComponent } from './pages/class/class-register/class-register.component';
import { CourseRegisterComponent } from './pages/course/course-register/course-register.component';
import { LessonRegisterComponent } from './pages/lesson/lesson-register/lesson-register.component';
import { StudentRegisterComponent } from './pages/student/student-register/student-register.component';
import { SubjectRegisterComponent } from './pages/subject/subject-register/subject-register.component';
import { TeacherRegisterComponent } from './pages/teacher/teacher-register/teacher-register.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    SubjectComponent,
    TeacherComponent,
    LessonComponent,
    ClassComponent,
    StudentComponent,
    SidebarComponent,
    HomeComponent,
    CourseComponent,
    ClassRegisterComponent,
    CourseRegisterComponent,
    LessonRegisterComponent,
    StudentRegisterComponent,
    SubjectRegisterComponent,
    TeacherRegisterComponent,
    NavbarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [
    provideClientHydration()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
