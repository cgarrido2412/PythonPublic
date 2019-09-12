#tchu
Try{
    # Try a series of statement codes here... and/or ForEach etc. 

    # Last line of the block code
    $status = "Successfully exectued the try block code without any error."
}
Catch{
    # If try block ran into exception, it will execute it here. 
    $status = "$($_.Exception.Message)"
    Write-Host "Exception Message: $status"
}
Finally{
    Write-Host $status
}
