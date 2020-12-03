<span class="pl-k">import</span> <span class="pl-smi">org.asynchttpclient.*</span>;

<span class="pl-c"><span class="pl-c">//</span> bound</span>
<span class="pl-k">Future<<span class="pl-smi">Response</span>></span> whenResponse <span class="pl-k">=</span> asyncHttpClient<span class="pl-k">.</span>prepareGet(<span class="pl-s"><span class="pl-pds">"</span>http://www.example.com/<span class="pl-pds">"</span></span>)<span class="pl-k">.</span>execute();

<span class="pl-c"><span class="pl-c">//</span> unbound</span>
<span class="pl-smi">Request</span> request <span class="pl-k">=</span> get(<span class="pl-s"><span class="pl-pds">"</span>http://www.example.com/<span class="pl-pds">"</span></span>)<span class="pl-k">.</span>build();
<span class="pl-k">Future<<span class="pl-smi">Response</span>></span> whenResponse <span class="pl-k">=</span> asyncHttpClient<span class="pl-k">.</span>executeRequest(request);