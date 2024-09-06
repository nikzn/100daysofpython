       <mat-accordion [togglePosition]="'before'"> 
                      <mat-expansion-panel class="accordion" *ngFor="let item of flowboardNominators">
                        <mat-expansion-panel-header (click)="list360nominees(item)" >
                          <mat-panel-title>
                         {{item.managerName}}
                          </mat-panel-title>
                          <mat-panel-description>
                            <span  
                            [ngClass]="item.status=='Nomination Pending'?'cycle-360-assign-badge':item.status=='Nomination InProgress'?'cycle-360-approval-inprogress-badge':'cycle-360-completed-badge'"
                            > {{item.status}} </span> 
                          </mat-panel-description>
                        </mat-expansion-panel-header>
                     
                     
                      <table mat-table  [dataSource]="dataSource360"   class="mat-elevation-z8 table-striped" >

               

                          <!-- NOMINEE NAME -->
                        <ng-container matColumnDef="managerName">
                          <th mat-header-cell *matHeaderCellDef > Nominee </th>
                          <td mat-cell  class="dottext" *matCellDef="let element" > {{element.managerName}} </td>
                        </ng-container>
    
                        <!-- NOMINATED START DATE -->
                        <ng-container matColumnDef="nominationStartDate">
                          <th mat-header-cell *matHeaderCellDef > Nominated  </th>
                          <td mat-cell  class="dottext" *matCellDef="let element">
                            {{element.nominationStartDate| date : 'dd-MMM-yyyy'  }}
                          </td>
                        </ng-container>
    
                        <!-- NOMINATED END DATE -->
                        <ng-container matColumnDef="nominationEndDate">
                          <th mat-header-cell *matHeaderCellDef > Due  </th>
                          <td mat-cell  class="dottext" *matCellDef="let element">
                            {{element.nominationEndDate| date : 'dd-MMM-yyyy'  }}
                          </td>
                        </ng-container>
    
    
                        <!-- STATUS -->
                        <ng-container matColumnDef="status">
                          <th style="padding-left: 50px;" mat-header-cell *matHeaderCellDef > Status </th>
                          <td mat-cell  class="dottext" *matCellDef="let element" >
                            
                            <span [ngClass]="element.status=='Assign Nominee Pending'
                            ?'cycle-360-assign-badge':element.status=='In Progress'?
                            'cycle-360-approval-inprogress-badge':element.status=='Completed'?
                            'cycle-360-completed-badge':element.status=='Rejected'?
                            'cycle-360-rejected-badge':'cycle-360-approval-pending-badge'">{{element.status}}</span> </td>
                        </ng-container>
    

                        <!-- ACTION -->
                        <ng-container matColumnDef="actions">
                          <th mat-header-cell *matHeaderCellDef>Action</th>
                          <td mat-cell *matCellDef="let element" >
                           
                        
                            
                                <img src="../../../../../assets/img/removec.svg" class="review-icon icon-delete" *ngIf="element.isUserOwner==true&&element.status=='Response Pending'" pTooltip="Remove Nominee" (click)="onClickRemoveNominee(element)" >
                                <img class="review-icon" *ngIf="element.status=='Completed'"  src="../../../../../assets/img/View (1).svg" (click)="onClickRedirectToReview(element)" pTooltip="View Review"  alt="">

          
                             
                        
                          </td>
                        </ng-container>
    
    
                        <tr mat-header-row  *matHeaderRowDef="displayedColumns360"></tr>
                        <tr mat-row  *matRowDef="let row; columns: displayedColumns360;">
                    
                        </tr>
                        <tr class="mat-row" *matNoDataRow>
                          <td class="mat-cell" style="text-align:center" [attr.colspan]="columnsToDisplayWithExpand.length">No Data Found !!</td>
                    
                        </tr>
                        </table>
                      </mat-expansion-panel>
                      </mat-accordion>
