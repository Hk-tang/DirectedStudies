<span class="pl-k">import static</span> <span class="pl-smi">org.asynchttpclient.Dsl.*</span>;

<span class="pl-smi">AsyncHttpClient</span> c <span class="pl-k">=</span> asyncHttpClient(config()<span class="pl-k">.</span>setProxyServer(proxyServer(<span class="pl-s"><span class="pl-pds">"</span>127.0.0.1<span class="pl-pds">"</span></span>, <span class="pl-c1">38080</span>)));