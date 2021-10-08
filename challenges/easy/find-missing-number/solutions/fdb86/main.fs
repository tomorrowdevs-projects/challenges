module FindMissingNumber =

    let findMissing values= 
      let minList, maxList = (List.min values, List.max values)
      let newValues = [ minList .. maxList ]
      let missing = List.sum newValues - List.sum values
      missing
    
    
    
    let origList = [230; 222; 220; 224; 229; 221; 225; 223; 228; 226]


    printfn $"The missing number is: {findMissing origList}"