import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { ClassComponent } from './pages/register/class/class.component';
import { LessonComponent } from './pages/register/lesson/lesson.component';
import { StudentComponent } from './pages/register/student/student.component';
import { SubjectComponent } from './pages/register/subject/subject.component';
import { TeacherComponent } from './pages/register/teacher/teacher.component';
import { CourseComponent } from './pages/register/course/course.component';

const routes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'class', component: ClassComponent},
  {path: 'lesson', component: LessonComponent},
  {path: 'student', component: StudentComponent},
  {path: 'subject', component: SubjectComponent},
  {path: 'teacher', component: TeacherComponent},
  {path: 'course', component: CourseComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
