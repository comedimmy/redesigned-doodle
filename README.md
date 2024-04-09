# Python 期中報告第八題

  11124235 吳易軒 
  11124213 張芮瑜

# code
  ## 設定變數
    amount=1
    count=0
    i=1
    j=1
  ## 使用迴圈計算
    while i<=10:    //當i<=10
      print(i)      //印出當前i 
    
      amount *=i      //計算階乘 
    
      count+=amount   //將階乘結果再加到count 使其每次迴圈結束後變成1+2!+3!+4!+.....10!
    
      i+=1            //將i+1並再次返回while檢查i是否<=10

  ## 若i>10之後聽出迴圈並印出結果
    print("10!=",amount,"\n1+2!+3!+.....10!=",count)
