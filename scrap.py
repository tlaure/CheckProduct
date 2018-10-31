def check(productAdress):
  import requests
  pageHtml = requests.get(productAdress).text
  toFind="data-pv-product-stock-status"#Availability indicator on this website
  id1=pageHtml.find(toFind)
  result=pageHtml[id1+32:id1+40]
  if result=='outstock':
    ans=0
  else:
    ans=1

  return(ans)