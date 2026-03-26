const analyticsConfig = {
	provider: ga4,
	plausibleDomain: "",
	goatCounterEndpoint: "",
	gaMeasurementId: "G-RXESNWMH1Q",
};

(function initAnalytics() {
	if (
		typeof window === "undefined" ||
		!analyticsConfig.provider ||
		window.location.hostname === "localhost" ||
		window.location.hostname === "127.0.0.1"
	) {
		return;
	}

	function loadScript(src, attributes = {}) {
		if (document.querySelector(`script[src="${src}"]`)) {
			return;
		}

		const script = document.createElement("script");
		script.src = src;

		Object.entries(attributes).forEach(([key, value]) => {
			if (value !== undefined && value !== null && value !== "") {
				script.setAttribute(key, value);
			}
		});

		document.head.appendChild(script);
	}

	if (analyticsConfig.provider === "plausible" && analyticsConfig.plausibleDomain) {
		loadScript("https://plausible.io/js/script.js", {
			defer: "true",
			"data-domain": analyticsConfig.plausibleDomain,
		});
		return;
	}

	if (
		analyticsConfig.provider === "goatcounter" &&
		analyticsConfig.goatCounterEndpoint
	) {
		const endpoint = analyticsConfig.goatCounterEndpoint.replace(/\/$/, "");
		loadScript(`${endpoint}/count.js`, {
			async: "true",
			"data-goatcounter": `${endpoint}/count`,
		});
		return;
	}

	if (analyticsConfig.provider === "ga4" && analyticsConfig.gaMeasurementId) {
		const measurementId = analyticsConfig.gaMeasurementId;
		loadScript(`https://www.googletagmanager.com/gtag/js?id=${measurementId}`, {
			async: "true",
		});

		window.dataLayer = window.dataLayer || [];
		function gtag() {
			window.dataLayer.push(arguments);
		}

		gtag("js", new Date());
		gtag("config", measurementId);
	}
})();