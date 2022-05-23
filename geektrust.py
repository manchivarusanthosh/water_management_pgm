import sys

def calculate_water_bill_guests(guests):
    totalWaterForGuests = guests * 30 * 10
    costForGuests = 0
    while(totalWaterForGuests):
        if(totalWaterForGuests<=500):
            costForGuests += 500*2
            totalWaterForGuests=0
        elif(totalWaterForGuests>=501 and totalWaterForGuests<=1500):
            costForGuests += (totalWaterForGuests-500)*3
            totalWaterForGuests = 500
        elif(totalWaterForGuests>=1501 and totalWaterForGuests<=3000):
            costForGuests += (totalWaterForGuests-1500)*5 
            totalWaterForGuests = 1500
        elif(totalWaterForGuests>=3001):
            costForGuests +=  (totalWaterForGuests-3000)*8 
            totalWaterForGuests = 3000
    return costForGuests

def calculate_cost(numOfLitres):
    ratio = list(map(int,inputList[0][2].split(':')))
    cost = numOfLitres * (ratio[0]/(ratio[0]+ratio[1])) + numOfLitres * (ratio[1]/(ratio[0]+ratio[1])) * 1.5
    return cost

if __name__=="__main__":
    #variables
    inputList = []
    TotalCostForWater = 0
    TotalWater = 0
    total_guests = 0
    
    input_file = sys.argv[1]
    
    #accepting input from file

    f = open(input_file,'r')
    for line in f:
        inputList.append(line.split())
    

    # accepting input    
    # while(1):
    #     inputFromUser = input().split()
    #     inputList.append(inputFromUser)
    #     if 'BILL' in inputFromUser:
    #         break;
    
    #calculating cost for initial ratio
    if(inputList[0][1]=='2'):
        TotalWater = 3*10*30
        TotalCostForWater = calculate_cost(900)
        
    elif(inputList[0][1]=='3'):
        TotalWater =  (5*10*30)
        TotalCostForWater = (calculate_cost(1500))
        
    #calculating cost for GUESTS
    for eachList in inputList:
        if 'ADD_GUESTS' in eachList:
            total_guests+=int(eachList[1])
    
    #Final Result
    TotalWater +=total_guests*10*30
    TotalCostForWater+=calculate_water_bill_guests(total_guests)
    print(TotalWater,int(TotalCostForWater))
    
    
