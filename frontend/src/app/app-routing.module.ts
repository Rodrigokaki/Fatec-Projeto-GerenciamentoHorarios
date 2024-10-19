import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { ClassComponent } from './pages/class/class.component';
import { LessonComponent } from './pages/lesson/lesson.component';
import { StudentComponent } from './pages/student/student.component';
import { SubjectComponent } from './pages/subject/subject.component';
import { TeacherComponent } from './pages/teacher/teacher.component';
import { CourseComponent } from './pages/course/course.component';
import { CourseRegisterComponent } from './pages/course/course-register/course-register.component';
import { TeacherRegisterComponent } from './pages/teacher/teacher-register/teacher-register.component';
import { SubjectRegisterComponent } from './pages/subject/subject-register/subject-register.component';
import { StudentRegisterComponent } from './pages/student/student-register/student-register.component';
import { LessonRegisterComponent } from './pages/lesson/lesson-register/lesson-register.component';
import { ClassRegisterComponent } from './pages/class/class-register/class-register.component';

const routes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'class', component: ClassComponent},
  {path: 'class/register', component: ClassRegisterComponent},
  {path: 'lesson', component: LessonComponent},
  {path: 'lesson/register', component: LessonRegisterComponent},
  {path: 'student', component: StudentComponent},
  {path: 'student/register', component: StudentRegisterComponent},
  {path: 'subject', component: SubjectComponent},
  {path: 'subject/register', component: SubjectRegisterComponent},
  {path: 'teacher', component: TeacherComponent},
  {path: 'teacher/register', component: TeacherRegisterComponent},
  {path: 'course', component: CourseComponent},
  {path: 'course/register', component: CourseRegisterComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
