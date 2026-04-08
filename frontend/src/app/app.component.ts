import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AttritionService, AttritionResponse } from './attrition.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
  attritionForm!: FormGroup;
  predictionResult: AttritionResponse | null = null;
  loading = false;
  error: string | null = null;

  constructor(
    private fb: FormBuilder,
    private attritionService: AttritionService
  ) {}

  ngOnInit(): void {
    this.initForm();
  }

  private initForm(): void {
    this.attritionForm = this.fb.group({
      Age: [54, [Validators.required, Validators.min(18), Validators.max(100)]],
      BusinessTravel: ['Travel_Rarely', Validators.required],
      DailyRate: [800, [Validators.required, Validators.min(100)]],
      Department: ['Sales', Validators.required],
      DistanceFromHome: [5, [Validators.required, Validators.min(1)]],
      Education: [3, [Validators.required, Validators.min(1), Validators.max(5)]],
      EducationField: ['Life Sciences', Validators.required],
      EnvironmentSatisfaction: [4, [Validators.required, Validators.min(1), Validators.max(4)]],
      Gender: ['Male', Validators.required],
      HourlyRate: [70, [Validators.required, Validators.min(30)]],
      JobInvolvement: [3, [Validators.required, Validators.min(1), Validators.max(4)]],
      JobLevel: [2, [Validators.required, Validators.min(1), Validators.max(5)]],
      JobRole: ['Sales Executive', Validators.required],
      JobSatisfaction: [4, [Validators.required, Validators.min(1), Validators.max(4)]],
      MaritalStatus: ['Married', Validators.required],
      MonthlyIncome: [5000, [Validators.required, Validators.min(1000)]],
      MonthlyRate: [10000, [Validators.required, Validators.min(1000)]],
      NumCompaniesWorked: [1, [Validators.required, Validators.min(0)]],
      OverTime: ['No', Validators.required],
      PercentSalaryHike: [15, [Validators.required, Validators.min(0)]],
      PerformanceRating: [3, [Validators.required, Validators.min(1), Validators.max(4)]],
      RelationshipSatisfaction: [3, [Validators.required, Validators.min(1), Validators.max(4)]],
      StockOptionLevel: [1, [Validators.required, Validators.min(0), Validators.max(3)]],
      TotalWorkingYears: [10, [Validators.required, Validators.min(0)]],
      TrainingTimesLastYear: [3, [Validators.required, Validators.min(0), Validators.max(6)]],
      WorkLifeBalance: [3, [Validators.required, Validators.min(1), Validators.max(4)]],
      YearsAtCompany: [5, [Validators.required, Validators.min(0)]],
      YearsInCurrentRole: [2, [Validators.required, Validators.min(0)]],
      YearsSinceLastPromotion: [1, [Validators.required, Validators.min(0)]],
      YearsWithCurrManager: [2, [Validators.required, Validators.min(0)]]
    });
  }

  onSubmit(): void {
    if (this.attritionForm.invalid) return;

    this.loading = true;
    this.error = null;
    this.predictionResult = null;

    this.attritionService.predict(this.attritionForm.value).subscribe({
      next: (res) => {
        this.predictionResult = res;
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Prediction failed. Is the backend running?';
        this.loading = false;
        console.error(err);
      }
    });
  }
}
