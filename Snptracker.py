

import streamlit as st
import csv
import io
import pandas as pd

st.set_page_config(page_title="NutraSNP Tracker", layout="wide")
st.title("🧬 NutraSNP Tracker")


snp_annotations = {
    'rs1544410': {
        'gene': 'VDR',
        'nutrient': 'Vitamin D',
        'impact': 'Reduced vitamin D receptor function',
        'recommendation': 'Consider vitamin D3 supplements'
    },
    'rs2228570': {
        'gene': 'VDR',
        'nutrient': 'Vitamin D',
        'impact': 'Affects vitamin D metabolism',
        'recommendation': 'Monitor vitamin D levels regularly'
    },
    'rs1801133': {
        'gene': 'MTHFR',
        'nutrient': 'Folate',
        'impact': 'Poor folate conversion',
        'recommendation': 'Take methylated folate; eat leafy greens'
    },
    'rs1801131': {
        'gene': 'MTHFR',
        'nutrient': 'Folate',
        'impact': 'Intermediate folate metabolism',
        'recommendation': 'Moderate supplementation may help'
    },
    'rs4988235': {
        'gene': 'LCT',
        'nutrient': 'Lactose',
        'impact': 'Reduced lactase production',
        'recommendation': 'Try lactose-free dairy or enzyme supplements'
    },
    'rs1799945': {
        'gene': 'HFE',
        'nutrient': 'Iron',
        'impact': 'Risk of iron overload',
        'recommendation': 'Avoid iron supplements unless tested'
    },
    'rs174537': {
        'gene': 'FADS1',
        'nutrient': 'Omega-3 fatty acids',
        'impact': 'Lower DHA synthesis',
        'recommendation': 'Consume EPA/DHA from fish or algae oils'
    },
    'rs762551': {
        'gene': 'CYP1A2',
        'nutrient': 'Caffeine',
        'impact': 'Fast caffeine metabolism',
        'recommendation': 'Higher caffeine tolerance'
    },
    'rs738409': {
        'gene': 'PNPLA3',
        'nutrient': 'Vitamin E',
        'impact': 'Liver fat accumulation risk',
        'recommendation': 'Consider vitamin E under supervision'
    },
    'rs9939609': {
        'gene': 'FTO',
        'nutrient': 'General metabolism',
        'impact': 'Increased risk of obesity',
        'recommendation': 'Focus on physical activity and diet'
    },
    'rs1000011': {
        'gene': 'GENE11',
        'nutrient': 'Nutrient1',
        'impact': 'Mock impact description 11',
        'recommendation': 'Mock recommendation for SNP 11'
    },
    'rs1000012': {
        'gene': 'GENE12',
        'nutrient': 'Nutrient2',
        'impact': 'Mock impact description 12',
        'recommendation': 'Mock recommendation for SNP 12'
    },
    'rs1000013': {
        'gene': 'GENE13',
        'nutrient': 'Nutrient3',
        'impact': 'Mock impact description 13',
        'recommendation': 'Mock recommendation for SNP 13'
    },
    'rs1000014': {
        'gene': 'GENE14',
        'nutrient': 'Nutrient4',
        'impact': 'Mock impact description 14',
        'recommendation': 'Mock recommendation for SNP 14'
    },
    'rs1000015': {
        'gene': 'GENE15',
        'nutrient': 'Nutrient5',
        'impact': 'Mock impact description 15',
        'recommendation': 'Mock recommendation for SNP 15'
    },
    'rs1000016': {
        'gene': 'GENE16',
        'nutrient': 'Nutrient6',
        'impact': 'Mock impact description 16',
        'recommendation': 'Mock recommendation for SNP 16'
    },
    'rs1000017': {
        'gene': 'GENE17',
        'nutrient': 'Nutrient7',
        'impact': 'Mock impact description 17',
        'recommendation': 'Mock recommendation for SNP 17'
    },
    'rs1000018': {
        'gene': 'GENE18',
        'nutrient': 'Nutrient8',
        'impact': 'Mock impact description 18',
        'recommendation': 'Mock recommendation for SNP 18'
    },
    'rs1000019': {
        'gene': 'GENE19',
        'nutrient': 'Nutrient9',
        'impact': 'Mock impact description 19',
        'recommendation': 'Mock recommendation for SNP 19'
    },
    'rs1000020': {
        'gene': 'GENE20',
        'nutrient': 'Nutrient0',
        'impact': 'Mock impact description 20',
        'recommendation': 'Mock recommendation for SNP 20'
    },
    'rs1000021': {
        'gene': 'GENE21',
        'nutrient': 'Nutrient1',
        'impact': 'Mock impact description 21',
        'recommendation': 'Mock recommendation for SNP 21'
    },
    'rs1000022': {
        'gene': 'GENE22',
        'nutrient': 'Nutrient2',
        'impact': 'Mock impact description 22',
        'recommendation': 'Mock recommendation for SNP 22'
    },
    'rs1000023': {
        'gene': 'GENE23',
        'nutrient': 'Nutrient3',
        'impact': 'Mock impact description 23',
        'recommendation': 'Mock recommendation for SNP 23'
    },
    'rs1000024': {
        'gene': 'GENE24',
        'nutrient': 'Nutrient4',
        'impact': 'Mock impact description 24',
        'recommendation': 'Mock recommendation for SNP 24'
    },
    'rs1000025': {
        'gene': 'GENE25',
        'nutrient': 'Nutrient5',
        'impact': 'Mock impact description 25',
        'recommendation': 'Mock recommendation for SNP 25'
    },
    'rs1000026': {
        'gene': 'GENE26',
        'nutrient': 'Nutrient6',
        'impact': 'Mock impact description 26',
        'recommendation': 'Mock recommendation for SNP 26'
    },
    'rs1000027': {
        'gene': 'GENE27',
        'nutrient': 'Nutrient7',
        'impact': 'Mock impact description 27',
        'recommendation': 'Mock recommendation for SNP 27'
    },
    'rs1000028': {
        'gene': 'GENE28',
        'nutrient': 'Nutrient8',
        'impact': 'Mock impact description 28',
        'recommendation': 'Mock recommendation for SNP 28'
    },
    'rs1000029': {
        'gene': 'GENE29',
        'nutrient': 'Nutrient9',
        'impact': 'Mock impact description 29',
        'recommendation': 'Mock recommendation for SNP 29'
    },
    'rs1000030': {
        'gene': 'GENE30',
        'nutrient': 'Nutrient0',
        'impact': 'Mock impact description 30',
        'recommendation': 'Mock recommendation for SNP 30'
    },
    'rs1000031': {
        'gene': 'GENE31',
        'nutrient': 'Nutrient1',
        'impact': 'Mock impact description 31',
        'recommendation': 'Mock recommendation for SNP 31'
    },
    'rs1000032': {
        'gene': 'GENE32',
        'nutrient': 'Nutrient2',
        'impact': 'Mock impact description 32',
        'recommendation': 'Mock recommendation for SNP 32'
    },
    'rs1000033': {
        'gene': 'GENE33',
        'nutrient': 'Nutrient3',
        'impact': 'Mock impact description 33',
        'recommendation': 'Mock recommendation for SNP 33'
    },
    'rs1000034': {
        'gene': 'GENE34',
        'nutrient': 'Nutrient4',
        'impact': 'Mock impact description 34',
        'recommendation': 'Mock recommendation for SNP 34'
    },
    'rs1000035': {
        'gene': 'GENE35',
        'nutrient': 'Nutrient5',
        'impact': 'Mock impact description 35',
        'recommendation': 'Mock recommendation for SNP 35'
    },
    'rs1000036': {
        'gene': 'GENE36',
        'nutrient': 'Nutrient6',
        'impact': 'Mock impact description 36',
        'recommendation': 'Mock recommendation for SNP 36'
    },
    'rs1000037': {
        'gene': 'GENE37',
        'nutrient': 'Nutrient7',
        'impact': 'Mock impact description 37',
        'recommendation': 'Mock recommendation for SNP 37'
    },
    'rs1000038': {
        'gene': 'GENE38',
        'nutrient': 'Nutrient8',
        'impact': 'Mock impact description 38',
        'recommendation': 'Mock recommendation for SNP 38'
    },
    'rs1000039': {
        'gene': 'GENE39',
        'nutrient': 'Nutrient9',
        'impact': 'Mock impact description 39',
        'recommendation': 'Mock recommendation for SNP 39'
    },
    'rs1000040': {
        'gene': 'GENE40',
        'nutrient': 'Nutrient0',
        'impact': 'Mock impact description 40',
        'recommendation': 'Mock recommendation for SNP 40'
    },
    'rs1000041': {
        'gene': 'GENE41',
        'nutrient': 'Nutrient1',
        'impact': 'Mock impact description 41',
        'recommendation': 'Mock recommendation for SNP 41'
    },
    'rs1000042': {
        'gene': 'GENE42',
        'nutrient': 'Nutrient2',
        'impact': 'Mock impact description 42',
        'recommendation': 'Mock recommendation for SNP 42'
    },
    'rs1000043': {
        'gene': 'GENE43',
        'nutrient': 'Nutrient3',
        'impact': 'Mock impact description 43',
        'recommendation': 'Mock recommendation for SNP 43'
    },
    'rs1000044': {
        'gene': 'GENE44',
        'nutrient': 'Nutrient4',
        'impact': 'Mock impact description 44',
        'recommendation': 'Mock recommendation for SNP 44'
    },
    'rs1000045': {
        'gene': 'GENE45',
        'nutrient': 'Nutrient5',
        'impact': 'Mock impact description 45',
        'recommendation': 'Mock recommendation for SNP 45'
    },
    'rs1000046': {
        'gene': 'GENE46',
        'nutrient': 'Nutrient6',
        'impact': 'Mock impact description 46',
        'recommendation': 'Mock recommendation for SNP 46'
    },
    'rs1000047': {
        'gene': 'GENE47',
        'nutrient': 'Nutrient7',
        'impact': 'Mock impact description 47',
        'recommendation': 'Mock recommendation for SNP 47'
    },
    'rs1000048': {
        'gene': 'GENE48',
        'nutrient': 'Nutrient8',
        'impact': 'Mock impact description 48',
        'recommendation': 'Mock recommendation for SNP 48'
    },
    'rs1000049': {
        'gene': 'GENE49',
        'nutrient': 'Nutrient9',
        'impact': 'Mock impact description 49',
        'recommendation': 'Mock recommendation for SNP 49'
    },
    'rs1000050': {
        'gene': 'GENE50',
        'nutrient': 'Nutrient0',
        'impact': 'Mock impact description 50',
        'recommendation': 'Mock recommendation for SNP 50'
    },
    'rs1000051': {
        'gene': 'GENE51',
        'nutrient': 'Nutrient1',
        'impact': 'Mock impact description 51',
        'recommendation': 'Mock recommendation for SNP 51'
    },
    'rs1000052': {
        'gene': 'GENE52',
        'nutrient': 'Nutrient2',
        'impact': 'Mock impact description 52',
        'recommendation': 'Mock recommendation for SNP 52'
    },
    'rs1000053': {
        'gene': 'GENE53',
        'nutrient': 'Nutrient3',
        'impact': 'Mock impact description 53',
        'recommendation': 'Mock recommendation for SNP 53'
    },
    'rs1000054': {
        'gene': 'GENE54',
        'nutrient': 'Nutrient4',
        'impact': 'Mock impact description 54',
        'recommendation': 'Mock recommendation for SNP 54'
    },
    'rs1000055': {
        'gene': 'GENE55',
        'nutrient': 'Nutrient5',
        'impact': 'Mock impact description 55',
        'recommendation': 'Mock recommendation for SNP 55'
    },
    'rs1000056': {
        'gene': 'GENE56',
        'nutrient': 'Nutrient6',
        'impact': 'Mock impact description 56',
        'recommendation': 'Mock recommendation for SNP 56'
    },
    'rs1000057': {
        'gene': 'GENE57',
        'nutrient': 'Nutrient7',
        'impact': 'Mock impact description 57',
        'recommendation': 'Mock recommendation for SNP 57'
    },
    'rs1000058': {
        'gene': 'GENE58',
        'nutrient': 'Nutrient8',
        'impact': 'Mock impact description 58',
        'recommendation': 'Mock recommendation for SNP 58'
    },
    'rs1000059': {
        'gene': 'GENE59',
        'nutrient': 'Nutrient9',
        'impact': 'Mock impact description 59',
        'recommendation': 'Mock recommendation for SNP 59'
    },
    'rs1000060': {
        'gene': 'GENE60',
        'nutrient': 'Nutrient0',
        'impact': 'Mock impact description 60',
        'recommendation': 'Mock recommendation for SNP 60'
    },
    'rs1000061': {
        'gene': 'GENE61',
        'nutrient': 'Nutrient1',
        'impact': 'Mock impact description 61',
        'recommendation': 'Mock recommendation for SNP 61'
    },
    'rs1000062': {
        'gene': 'GENE62',
        'nutrient': 'Nutrient2',
        'impact': 'Mock impact description 62',
        'recommendation': 'Mock recommendation for SNP 62'
    },
    'rs1000063': {
        'gene': 'GENE63',
        'nutrient': 'Nutrient3',
        'impact': 'Mock impact description 63',
        'recommendation': 'Mock recommendation for SNP 63'
    },
    'rs1000064': {
        'gene': 'GENE64',
        'nutrient': 'Nutrient4',
        'impact': 'Mock impact description 64',
        'recommendation': 'Mock recommendation for SNP 64'
    },
    'rs1000065': {
        'gene': 'GENE65',
        'nutrient': 'Nutrient5',
        'impact': 'Mock impact description 65',
        'recommendation': 'Mock recommendation for SNP 65'
    },
    'rs1000066': {
        'gene': 'GENE66',
        'nutrient': 'Nutrient6',
        'impact': 'Mock impact description 66',
        'recommendation': 'Mock recommendation for SNP 66'
    },
    'rs1000067': {
        'gene': 'GENE67',
        'nutrient': 'Nutrient7',
        'impact': 'Mock impact description 67',
        'recommendation': 'Mock recommendation for SNP 67'
    },
    'rs1000068': {
        'gene': 'GENE68',
        'nutrient': 'Nutrient8',
        'impact': 'Mock impact description 68',
        'recommendation': 'Mock recommendation for SNP 68'
    },
    'rs1000069': {
        'gene': 'GENE69',
        'nutrient': 'Nutrient9',
        'impact': 'Mock impact description 69',
        'recommendation': 'Mock recommendation for SNP 69'
    }
}

# To avoid long scroll, assuming you already defined `snp_annotations` as provided earlier

# ---- Upload Section ----
uploaded_file = st.file_uploader("📁 Upload your SNP CSV file", type="csv")

if uploaded_file:
    file_text = uploaded_file.read().decode("utf-8-sig")  # Handles BOM from Excel exports
    st.success("✅ File uploaded successfully!")

    csv_reader = csv.DictReader(io.StringIO(file_text))
    data = list(csv_reader)

    if not data or 'SNP ID' not in data[0]:
        st.error("❌ Your CSV must have a 'SNP ID' column.")
        st.stop()

    df = pd.DataFrame(data)
    st.write("### 👁️ Preview of Uploaded Data")
    st.dataframe(df.head(20))  # Show first 20 rows

    # ---- SNP Search ----
    user_input = st.text_input("🔍 Enter SNP ID to search (e.g., rs1544410)")

    if user_input:
        query = user_input.strip().lower()
        matches = [row for row in data if row['SNP ID'].strip().lower() == query]

        if matches:
            st.success("✅ SNP found in your file:")
            st.write(matches[0])

            if query in snp_annotations:
                annotation = snp_annotations[query]
                st.markdown("### 📌 Annotation from NutraDatabase")
                st.write(f"**Gene:** {annotation['gene']}")
                st.write(f"**Nutrient Affected:** {annotation['nutrient']}")
                st.write(f"**Impact:** {annotation['impact']}")
                st.write(f"**Recommendation:** {annotation['recommendation']}")
            else:
                st.info("ℹ️ No annotation found in the database for this SNP.")
        else:
            st.warning("⚠️ SNP not found in your uploaded file.")

    # ---- Show All Annotated SNPs ----
    st.markdown("---")
    if st.button("🔎 Show All Annotated SNPs in My File"):
        annotated_matches = []
        for row in data:
            snp_id = row['SNP ID'].strip().lower()
            if snp_id in snp_annotations:
                annotated_row = row.copy()
                annotated_row.update(snp_annotations[snp_id])
                annotated_matches.append(annotated_row)

        if annotated_matches:
            annotated_df = pd.DataFrame(annotated_matches)
            st.write(f"### 🧾 Found {len(annotated_matches)} annotated SNPs in your file:")
            st.dataframe(annotated_df)

            # Optional: Download CSV button
            csv_out = annotated_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Annotated SNPs CSV",
                data=csv_out,
                file_name="annotated_snps.csv",
                mime='text/csv'
            )
        else:
            st.warning("😕 No SNPs from your file matched our annotation database.")
else:
    st.info("👆 Please upload a CSV file to begin.")
