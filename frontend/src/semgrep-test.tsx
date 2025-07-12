import React from "react";

function SemgrepTest() {
  // Vulnerable example: bypass TLS verification
  process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";

  // Vulnerable: eval usage
  const userInput = "alert('Hacked!')";
  eval(userInput);

  // Vulnerable: hardcoded secret
  const API_KEY = "12345-ABCDE-SECRET-KEY";

  // Vulnerable: dangerouslySetInnerHTML XSS
  const userHtml = "<img src=x onerror=alert('XSS') />";

  return (
    <div>
      <h1>Semgrep Vulnerability Test</h1>
      <div dangerouslySetInnerHTML={{ __html: userHtml }} />
      <p>API Key: {API_KEY}</p>
    </div>
  );
}

export default SemgrepTest;
