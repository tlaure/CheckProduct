from interact import sendmail
from scrap import check
who="thomas.laure@me.com" #mail adrees on which the alert will be sent
productAdress="https://fr.louisvuitton.com/fra-fr/produits/chemise-hunting-nvprod1070059v" #product to check
isSellable=check(productAdress)#Check if product is available
if isSellable==1:
  sendmail(who,productAdress)#If available send a mail