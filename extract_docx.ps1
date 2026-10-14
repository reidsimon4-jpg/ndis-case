Add-Type -AssemblyName System.IO.Compression.FileSystem
$docxPath = "c:\Users\simon\Desktop\ndis case\AAT transcript.docx"
$zip = [System.IO.Compression.ZipFile]::OpenRead($docxPath)
$entry = $zip.Entries | Where-Object { $_.FullName -eq "word/document.xml" }
$stream = $entry.Open()
$reader = New-Object System.IO.StreamReader($stream)
$content = $reader.ReadToEnd()
$reader.Close()
$stream.Close()
$zip.Dispose()
$text = $content -replace '<[^>]+>', ' ' -replace '\s+', ' '
$text | Out-File "c:\Users\simon\Desktop\ndis case\AAT_transcript_text.txt" -Encoding UTF8
