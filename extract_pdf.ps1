param(
    [string]$PdfPath,
    [string]$OutputPath
)

# Read PDF binary and extract text strings
$bytes = [System.IO.File]::ReadAllBytes($PdfPath)

# Convert to string, looking for text between BT and ET markers, and also raw text
$rawText = [System.Text.Encoding]::UTF8.GetString($bytes)

# Method 1: Extract text from PDF stream objects (between stream and endstream)
$matches = [regex]::Matches($rawText, 'stream\r?\n(.+?)\r?\nendstream', [System.Text.RegularExpressions.RegexOptions]::Singleline)

$allText = ""

# Method 2: Simple extraction of readable ASCII text sequences
$readable = ""
foreach ($b in $bytes) {
    if (($b -ge 32 -and $b -le 126) -or $b -eq 10 -or $b -eq 13) {
        $readable += [char]$b
    } else {
        if ($readable.Length -gt 3) {
            # Filter out PDF operators and binary-looking content
            $lines = $readable -split "`n"
            foreach ($line in $lines) {
                $trimmed = $line.Trim()
                # Keep lines that look like actual text content (has spaces, words)
                if ($trimmed.Length -gt 20 -and ($trimmed -match '[a-zA-Z]{3,}\s+[a-zA-Z]{3,}')) {
                    $allText += $trimmed + "`n"
                }
            }
        }
        $readable = ""
    }
}

# Process any remaining
if ($readable.Length -gt 3) {
    $lines = $readable -split "`n"
    foreach ($line in $lines) {
        $trimmed = $line.Trim()
        if ($trimmed.Length -gt 20 -and ($trimmed -match '[a-zA-Z]{3,}\s+[a-zA-Z]{3,}')) {
            $allText += $trimmed + "`n"
        }
    }
}

$allText | Out-File $OutputPath -Encoding UTF8
Write-Host "Extracted text to $OutputPath ($(($allText).Length) chars)"
