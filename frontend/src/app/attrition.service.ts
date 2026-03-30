import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface AttritionResponse {
  attrition: string;
  probability: number;
  prediction_class: number;
}

@Injectable({
  providedIn: 'root'
})
export class AttritionService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  predict(employeeData: any): Observable<AttritionResponse> {
    return this.http.post<AttritionResponse>(`${this.apiUrl}/predict`, employeeData);
  }

  checkHealth(): Observable<any> {
    return this.http.get(`${this.apiUrl}/health`);
  }
}
