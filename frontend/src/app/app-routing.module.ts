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

export const routes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'class', component: ClassComponent, data: {title: "Turmas"}},
  {path: 'class/register', component: ClassRegisterComponent, data: {title: "Cadastrar turma", isEditing: false}},
  {path: 'lesson', component: LessonComponent, data: {title: "Aulas"}},
  {path: 'lesson/register', component: LessonRegisterComponent, data: {title: "Cadastrar aula", isEditing: false}},
  {path: 'student', component: StudentComponent, data: {title: "Alunos"}},
  {path: 'student/register', component: StudentRegisterComponent, data: {title: "Cadastrar aluno", isEditing: false}},
  {path: 'subject', component: SubjectComponent, data: {title: "Disciplinas"}},
  {path: 'subject/register', component: SubjectRegisterComponent, data: {title: "Cadastrar disciplina", isEditing: false}},
  {path: 'teacher', component: TeacherComponent, data: {title: "Professores"}},
  {path: 'teacher/register', component: TeacherRegisterComponent, data: {title: "Cadastrar professor", isEditing: false}},
  {path: 'course', component: CourseComponent, data: {title: "Cursos"}},
  {path: 'course/register', component: CourseRegisterComponent, data: {title: "Cadastrar curso", isEditing: false}}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
